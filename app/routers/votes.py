from fastapi import HTTPException, Response, status, Depends, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .. import schemas, models, utils, oauth2
from ..database import get_db

router = APIRouter(prefix="/votes", tags=["Votes"])

@router.post("/")
def do_vote(vote: schemas.VoteCreate, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {vote.post_id} was not found",
        )

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    db_vote = vote_query.first()
    if (vote.vote):
        if db_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted post {vote.post_id}")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=schemas.Vote(user_id=new_vote.user_id, post_id=new_vote.post_id).model_dump())
    else:
        if not db_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has not voted post {vote.post_id}")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)



        
