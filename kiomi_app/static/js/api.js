const url = "http://127.0.0.1:8000/api";

const getProducts = (currentPage) => {
  const endpoint = `${url}/products/?page=${currentPage}`;
  return fetch(endpoint)
    .then((res) => res.json())
    .then((res) => res);
};
/* Product Details */
const getProductDetails = (id) => {
  const endpoint = `${url}/products-detail/${id}/`;
  return fetch(endpoint)
    .then((res) => res.json())
    .then((res) => res);
};

const getOrderItems = () => {
  const endpoint = `${url}/order-item-get/`;
  return fetch(endpoint)
    .then((res) => res.json())
    .then((res) => res);
};

/* Este fetch fue creado para hacer uso del metodo GET pero
del api order-item-post, este se requiere para hacer el update en el carrito */
const getOrderItemUpdate = (id) => {
  const endpoint = `${url}/order-item-post/${id}/`;
  return fetch(endpoint)
    .then((res) => res.json())
    .then((res) => res);
};

const postPorductOrderItems = (orderItems) => {
  const payload = JSON.stringify(orderItems);
  const endpoint = `${url}/order-item-post/`;
  const csrfToken = Cookies.get("csrftoken");
  console.log(csrfToken);
  const headers = {
    "Content-Type": "application/json",
    "X-CSRFToken": csrfToken,
  };
  const requestOptions = {
    method: "POST",
    headers,
    body: payload,
  };
  return fetch(endpoint, requestOptions)
    .then((res) => res.json())
    .then((res) => console.log(res));
};

const putProductOrderItems = (orderItems, id) => {
  const payload = JSON.stringify(orderItems);
  const endpoint = `${url}/order-item-post/` + id + `/`;
  const csrfToken = Cookies.get("csrftoken");
  console.log(csrfToken);
  const headers = {
    "Content-Type": "application/json",
    "X-CSRFToken": csrfToken,
  };
  const requestOptions = {
    method: "PUT",
    headers,
    body: payload,
  };
  return fetch(endpoint, requestOptions)
    .then((res) => res.json())
    .then((res) => res);
};

const deleteProductOrderItems = (id) => {
  const endpoint = `${url}/order-item-post/` + id + `/`;
  const csrfToken = Cookies.get("csrftoken");
  //console.log(csrfToken);
  const headers = {
    "Content-Type": "application/json",
    "X-CSRFToken": csrfToken,
  };
  const requestOptions = {
    method: "DELETE",
    headers,
  };
  return fetch(endpoint, requestOptions)
    .then((res) => res.json())
    .then((res) => res);
};

export default {
  getProducts,
  getProductDetails,
  postPorductOrderItems,
  getOrderItems,
  putProductOrderItems,
  deleteProductOrderItems,
  getOrderItemUpdate,
};
