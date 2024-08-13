from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database
from fastapi.responses import RedirectResponse

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/shorten", response_model=schemas.URL)
def create_short_url(url: schemas.URLCreate, db: Session = Depends(database.get_db)):
    db_url = crud.create_short_url(db=db, long_url=url.long_url)
    return db_url

@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(database.get_db)):
    db_url = crud.get_url_by_short_code(db, short_code)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=db_url.long_url)
