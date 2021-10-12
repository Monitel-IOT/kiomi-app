import api from "../api.js";
new Vue({
  delimiters: ["[[", "]]"],
  el: "#car",
  data() {
    return {
      dbOrderItems: [],
      subTotal: 0,
      subTotalPorItem: [],
    };
  },
  created() {
    api.getOrderItems().then((orderItems) => {
      this.dbOrderItems = orderItems;
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

    deleteItem(id) {
      console.log(id);
      api.deleteProductOrderItems(id);
      const newDbOrderItems = this.dbOrderItems.filter((el) => el.id !== id);
      this.dbOrderItems = newDbOrderItems;
    },

    updateItemQuantity(newQuantity, indexArray, idAtrr) {
      //let dbOrderItemUpdate;
      api.getOrderItemUpdate(idAtrr).then((orderItems) => {
        const dbOrderItemUpdate = orderItems;
        dbOrderItemUpdate.quantity = newQuantity;
        api.putProductOrderItems(dbOrderItemUpdate, idAtrr);
        this.dbOrderItems[indexArray].quantity = newQuantity;
      });
    },

    canQuantityGoUp(quantity) {
      if (quantity < 99) {
        return true;
      }
      return false;
    },
    canQuantityGoDown(quantity) {
      if (quantity > 1) {
        return true;
      }
      return false;
    },
  },
});
