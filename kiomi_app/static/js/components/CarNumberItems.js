import api from "../api.js";
new Vue({
  delimiters: ["[[", "]]"],
  el: "#car-number-items",
  data() {
    return {
      dbOrderItems: [],
      numItemscarro: 0,
    };
  },
  created() {
    api.getOrderItems().then((orderitems) => {
      this.dbOrderItems = orderitems;
      this.numItemscarro = orderitems.length;
    });
  },

  watch: {
    // whenever question changes, this function will run
    dbOrderItems() {
      this.calcularNumItemsCarro();
    },
  },

  methods: {
    calcularNumItemsCarro() {
      let auxNumItems = this.dbOrderItems.length;
      this.numItemscarro = auxNumItems;
      return auxNumItems;
    },
  },
});
