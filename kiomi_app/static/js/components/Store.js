// import StoreCardProduct from './StoreCardProduct'

import api from '../api.js'


new Vue({
  delimiters: ['[[', ']]'],
  el: '#store',
  data() {
    return {
      dbProducts: [],
    }
  },
  created() {
    api
      .getProducts()
      .then((products) => 
      {console.log(products.results)
      this.dbProducts = products})
  },
})
