
from fastapi import FastAPI
from .routes import auth, tax_profile, upload

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(tax_profile.router, prefix="/tax-profile")
app.include_router(upload.router, prefix="/upload")

@app.get("/")
def root():
    return {"message": "TaxBox.AI API is running"}
