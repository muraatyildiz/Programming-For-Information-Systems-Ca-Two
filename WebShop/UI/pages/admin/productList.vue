

<template>
  <v-data-table
    :headers="headers"
    :items="products"
    sort-by="name"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Product List</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="1000px" :key="dialogKey">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
              New Product
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="12" md="6">
                    <v-text-field
                      v-model="product.name"
                      label="Product Name"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="6">
                    <v-text-field
                      v-model.number="product.price"
                      label="Price"
                      prefix="€"
                      type="number"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="6">
                    <v-select
                      v-model="product.category"
                      label="Category"
                      :items="['flowers', 'christmas', 'event']"
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="12" md="6">
                    <v-text-field
                      v-model.number="product.stock"
                      label="Stock"
                      type="number"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="12">
                    <v-textarea
                      clearable
                      clear-icon="mdi-close-circle"
                      v-model="product.description"
                      label="Description"
                      variant="outlined"
                      color="cyan"
                    ></v-textarea>
                  </v-col>
                  <v-col cols="12" sm="12" md="12">
                    <div>
                      <VueFileAgent
                        ref="vueFileAgent"
                        :theme="'grid'"
                        :multiple="true"
                        :deletable="true"
                        :meta="false"
                        :maxSize="'10MB'"
                        :linkable="true"
                        :maxFiles="1"
                        @beforedelete="onBeforeDelete($event)"
                        :helpText="'Choose img for the product'"
                        :errorText="{
                          type: 'Invalid file type. Only images or zip Allowed',
                          size: 'Files should not exceed 10MB in size',
                        }"
                        @select="filesSelected($event)"
                        @delete="fileDeleted($event)"
                        :disabled="false"
                        v-model="fileRecords"
                        accept="image/*"
                      >
                      </VueFileAgent>
                    </div>
                  </v-col>
                  <!-- <v-col cols="12" sm="12" md="12">
                    <v-img
                    
                      src="http://192.168.0.63:8080/file/serve-image/bolt-dumbbells-1.jpg" 
                    ></v-img>
                  </v-col> -->
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
              <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="800px">
          <v-card>
            <v-card-title class="text-h5"
              >Are you sure you want to delete this product?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete"
                >Cancel</v-btn
              >
              <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
      <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
    </template>
  </v-data-table>
</template>

<script>
export default {
  layout: "adminDefault",
  name: "productListPage",
  data: () => ({
    product: {
      id: 0,
      name: "",
      category: "",
      stock: null,
      price: null,
      imgUrl: "",
      description: "",
    },
    dialog: false,
    dialogDelete: false,
    fileRecordsForUpload: [],
    fileRecords: [],
    headers: [
      {
        text: "Products",
        align: "start",
        sortable: false,
        value: "name",
      },
      { text: "Price", value: "price" },
      { text: "Stock", value: "stock" },
      { text: "Description", value: "description" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    dialogKey: new Date().getTime(),
    products: [],
    editedIndex: -1,
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Product" : "Edit Product";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
      this.dialogKey = new Date().getTime();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  created() {
    this.getProductList();
  },
  methods: {
    getProductList() {
      let link = "product/list";
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          var answer = response.body;
          if (answer.count > 0) {
            this.products = answer.Results;
          }
        })
        .catch((x) => {
          console.log("Error");
        });
    },

    editItem(item) {
      this.dialogKey = new Date().getTime();
      this.editedIndex = this.products.indexOf(item);
      this.product = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.products.indexOf(item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      let id = this.products[this.editedIndex].id;
      let link = "product/delete/" + id;
      this.$store.dispatch("requestDelete", link).then((response) => {
        var answer = response.body;
        this.getProductList();
      });
      this.closeDelete();
    },
    close() {
      this.dialog = false;
      this.dialogKey = new Date().getTime();
      this.$nextTick(() => {
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        if (this.fileRecords.length > 0) {
          this.product.imgUrl = this.fileRecords[0].file.name;
        }
        let product = JSON.parse(JSON.stringify(this.product));
        let link = "product/update";
        let send = { link, data: product };
        console.log(product)
        this.$store.dispatch("requestPost", send).then((response) => {
          var answer = response.body;
          if (answer.Result == "Success") {
            this.getProductList();
          } else {
          }
        });
      } else {
        this.product.imgUrl = this.fileRecords[0].file.name;
        let product = JSON.parse(JSON.stringify(this.product));
        let link = "product/add";
        let send = { link, data: product };
        this.$store.dispatch("requestPost", send).then((response) => {
          var answer = response.body;
          if (answer.Result == "Success") {
            this.getProductList();
          } else {
          }
        });
      }
      this.dialogKey = new Date().getTime();
      this.close();
    },

    filesSelected: function (fileRecordsNewlySelected) {
      var validFileRecords = fileRecordsNewlySelected.filter(
        (fileRecord) => !fileRecord.error
      );

      this.fileRecordsForUpload =
        this.fileRecordsForUpload.concat(validFileRecords);
      let link = this.$store.state.ApiLink + "file/upload";
      let Token = "Bearer ";

      this.$refs.vueFileAgent
        .upload(link, { Authorization: Token }, this.fileRecordsForUpload)
        .then((f) => {
          this.fileRecordsForUpload = [];
        });
      console.log("files", this.fileRecordsForUpload);
    },
    fileDeleted: function (fileRecord) {
      console.log("here");
    },
    onBeforeDelete: function (fileRecord) {
      var i = this.fileRecordsForUpload.indexOf(fileRecord);
    },
  },
};
</script>
 
<style></style>
