from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.routes import router

app=FastAPI()

        
#CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)


app.include_router(router)

