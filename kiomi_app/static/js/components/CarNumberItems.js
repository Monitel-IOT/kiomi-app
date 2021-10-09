import api from "../api.js";
new Vue({
  delimiters: ["[[", "]]"],
  el: "#car-number-items",
  data() {
    return {
      dbOrderItems: [],
    };
  },
  created() {
    api.getOrderItems().then((orderitems) => {
      this.dbOrderItems = orderitems;
    });
  },

  methods: {
    calcularNumItemsCarro() {
      return this.dbOrderItems.length;
    },
  },
});
