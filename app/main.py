from fastapi import FastAPI


app = FastAPI()


@app.post('/get_form')
def get_form():
    return {'test': 'it is working'}
