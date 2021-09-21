import api from '../api.js'
import { LocalStorage } from '../utils/LocalStorage.js'

new Vue({
  delimiters: ["[[", "]]"],
  el: "#product-details",
  data() {
    return {
      dbProductDetails: [],
			imgPrincipal: 0,
			dbOrderItem: {},
			quantity: 0,
			flavor: ''
    }
  },
  created() {
		/*
			Obtener los detalles del producto de la api
		*/
    api
      .getProductDetails(this.idDetails())
      .then((product) => this.dbProductDetails = product)
  },
	watch: {
		/*
		* Observa cambios en quantiy
		*/
		quantity (newValue) {
			this.addDbOrderItem('quantity', newValue)
		},
		/*
		* Observa cambios en flavor
		*/
		flavor (newValue) {
			this.addDbOrderItem('flavor', newValue)
		}
	},
	methods: {
		/*
		*	Obtener el id pasado como query parmas, 
		*	de la url de la pagina actual.
		*/
		idDetails () {
			const search = window.location.search
			const urlParam = new URLSearchParams(search)
			return parseInt(urlParam.get('id'))
		},
		/*
		*	Añade un nuevo atributo al objeto dbOrderItem,
		*	parametros de entrada una clave y valor del atributo
		*/
		addDbOrderItem(key, value) {
			this.dbOrderItem = {
				...this.dbOrderItem, 
				[key]: value
			}
		},
		/*
		*	Evento del button ir al carrito, añade el objeto dbOrderItem
		* al localStorage del navegador
		*/
		handleGoCart() {
			LocalStorage.saveOrderItem(this.dbOrderItem)
		},
		changeImage(num) {
      this.imgPrincipal = num;
      // console.log(this.imgPrincipal);
    },
	}

})
