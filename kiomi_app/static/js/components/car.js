import api from "../api.js";
new Vue({
  delimiters: ["[[", "]]"],
  el: "#car",
  data() {
    return {
      dbOrderItems: [],
      dbProducts: [],
      /* flavor: "",
      flavorBizcocho: "",
      flavorCobertura: "",
      productName: "", */
    };
  },
  created() {
    api.getOrderItems().then((orderitems) => {
      this.dbOrderItems = orderitems;
      this.dbProducts = orderitems[0].product;
      console.log(this.dbProducts);
    });
  },

  methods: {},
});
