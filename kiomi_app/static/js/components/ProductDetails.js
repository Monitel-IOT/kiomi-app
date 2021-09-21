import api from "../api.js";

new Vue({
  delimiters: ["[[", "]]"],
  el: "#product-details",
  data() {
    return {
      dbProductDetails: [],
      message: "hello World!!",
      imgPrincipal: 0,
    };
  },
  created() {
    const search = window.location.search;
    const urlParam = new URLSearchParams(search);
    const id = parseInt(urlParam.get("id"));
    // console.log('id', id)
    api
      .getProductDetails(id)
      .then((product) => (this.dbProductDetails = product));
  },

  methods: {
    changeImage(num) {
      this.imgPrincipal = num;
      //console.log(this.imgPrincipal);
    },
  },
});
