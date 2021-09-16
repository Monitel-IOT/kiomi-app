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

export default {
	getProducts,
	getProductDetails,
}
