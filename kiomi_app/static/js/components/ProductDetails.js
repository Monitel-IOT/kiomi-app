import api from '../api.js'

new Vue({
  delimiters: ['[[', ']]'],
  el: '#product-details',
  data() {
    return {
      dbProductDetails: [],
			message: 'hello World!!'
    }
  },
  created() {
		const search = window.location.search
		const urlParam = new URLSearchParams(search)
		const id = parseInt(urlParam.get('id'))
		// console.log('id', id)
    api
      .getProductDetails(id)
      .then((product) => this.dbProductDetails = product)
  },


})