// import StoreCardProduct from './StoreCardProduct'
//  const currentPage= 1;

import api from "../api.js";
new Vue({
  delimiters: ["[[", "]]"],
  el: "#store",
  data() {
    return {
      dbProducts: [],
      nextPages: "",
    };
  },
  created() {
    const currentPage = 1;
    const search = window.location.search;
    const urlParam = new URLSearchParams(search);
    //console.log("hola",search);
    const page = parseInt(urlParam.get("page"));
    if (search === "") {
      const currentPage = 1;
      api.getProducts(currentPage).then((products) => {
        this.dbProducts = products;
        const urlSplit = this.dbProducts.next.split("/");
        this.nextPages = urlSplit[5];
        //this.countProducts = products.count
      });
    } else {
      const urlParam = new URLSearchParams(search);
      //console.log("hola",search);
      const page = parseInt(urlParam.get("page"));
      const currentPage = page;
      api.getProducts(currentPage).then((products) => {
        this.dbProducts = products;
        const urlSplit = this.dbProducts.next.split("/");
        this.nextPages = urlSplit[5];
        //this.countProducts = products.count
      });
    }
  },
});
