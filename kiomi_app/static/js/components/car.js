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

  methods: {},
});
