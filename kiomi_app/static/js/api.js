const url = 'http://127.0.0.1:8000/api'

const getProducts = () => {
	return fetch(`${url}/products/`)
		.then((res) => res.json())
		.then((res) => res)
}

export default {
	getProducts
}