const url = 'http://127.0.0.1:8000/api'
Vue.component('store-card-product', {
  	name: 'store-card-product',
	props: {
		product: {
			type: Object,
			default: () => {}
		}
	},
  	template:/*html*/`
	<div class="card-product col-sm-12 col-md-6 col-lg-4">
		<div class="card">
			<img :src="product.image_1" class="card-img-top" :alt="product.name">
      <div class="card-body">
 		    <h5 class="card-title">{{ product.name }}</h5>
  		  <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
  		  <a :href="'/product-details/?id='+product.id" class="btn btn-primary">Go somewhere</a>
  		</div>
		</div>
	</div>
	`,
})
