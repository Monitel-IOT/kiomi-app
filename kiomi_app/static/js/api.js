
const url = 'http://127.0.0.1:8000/api'

const getProducts = (currentPage) => {
	const endpoint = `${url}/products/?page=${currentPage}`
	return fetch(endpoint)
		.then((res) =>	res.json())
		.then((res) => res)
}
/* Product Details */
const getProductDetails = (id) => {
	const endpoint = `${url}/products-detail/${id}/`
	return fetch(endpoint)
		.then((res) => res.json())
		.then((res) => res)
}
const postPorductOrderItems = (orderItems) => {
	const payload = JSON.stringify(orderItems);
	const endpoint = `${url}/order-item/`
	const csrfToken = Cookies.get('csrftoken');
	console.log(csrfToken);
	const headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
    };
	const requestOptions = {
        method: 'POST',
        headers,
		body: payload
	}
	return fetch(endpoint,requestOptions)
		.then((res) => res.json())
		.then((res) => console.log(res))
}
export default {
	getProducts,
	getProductDetails,
	postPorductOrderItems
}