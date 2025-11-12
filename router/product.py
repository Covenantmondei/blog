from fastapi import APIRouter, Form
from fastapi.responses import PlainTextResponse, Response


router = APIRouter(
    prefix='/product',
    tags=['product']
)


product = ['watch', 'clothes', 'shoes']

@router.post("/new")
def create_product(name: str = Form(...)):
    product.append(name)
    return product

@router.get("/all")
def get_all_products():
    # return product
    data = " ".join(product)

    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response


@router.get("/{id}")
def get_product(id: int):

    if id > len(product):
        out = "Product not found!"
        return PlainTextResponse(content=out, media_type="text/plain")
    
    else:
        products = product[id]
        data = "".join(products)
        return Response(content=data, media_type="text/plain")