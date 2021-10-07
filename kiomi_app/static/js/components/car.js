import api from "../api.js";
new Vue({
  delimiters: ["[[", "]]"],
  el: "#car",
  data() {
    return {
      dbOrderItems: [],
      subTotal: 0,
    };
  },
  created() {
    api.getOrderItems().then((orderitems) => {
      this.dbOrderItems = orderitems;
    });
  },

  methods: {
    calcularSubTotal() {
      let auxSubTotal = 0.0;
      this.dbOrderItems.forEach(function (el, index) {
        auxSubTotal += el.product.price * el.quantity;
      });

      this.subTotal = auxSubTotal.toFixed(2);
      return this.subTotal;
    },
  },
});
