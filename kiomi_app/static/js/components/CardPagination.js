Vue.component('card-pagination', {
	name: 'card-pagination',
	props: {
		nextPages: {
			type: String,
		}
	},
	computed: {
		// a computed getter
		dividir: function () {
		  // `this` points to the vm instance
		  return [1,2,3,4,5]
		}
		
	},
	template: /*html*/`
	<nav aria-label="Page navigation example">
	<ul class="pagination justify-content-center">
		<li class="page-item" :class="nextPages==='?page=2'?'disabled':''">
			  <a class="page-link" tabindex="-1" aria-disabled="true">Previous</a>
		</li>
		<li class="page-item" v-for= "i in dividir" :class="nextPages.length===0?'active':'?page='+(i+1)===nextPages? 'active':''">
			<a class="page-item page-link" :href="'/?page='+i">{{i}}</a>
		</li>
		<li class="page-item">
			<a class="page-link " :href="nextPages">Next</a>
		</li>
		</ul>
		<p>{{nextPages.length}}</p>
	</nav>
	`
})