<template>
  <div>
    <ul v-show="errors.length > 0" class="errors">
      <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
    </ul>
    <div v-show="!errors.length">
      <h3>{{ list.name }}</h3>
      <p v-show="loading">Loading...</p>
      <ul class="list">
        <FavoriteMovieCell v-for="item in list" :key="item.title" :item="item" />
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import FavoriteMovieCell from "./FavoriteMovieCell.vue";
export default {
  components: {
    FavoriteMovieCell
  },
  data() {
    return {
      loading: true,
      errors: [],
      list: []
    };
  },
  created() {
    {
      axios
        .get(
          "http://localhost:5000/test"
        )
        .then(response => {
            console.log( response.data)
          this.list = response.data;
        });
    }
  }
};
</script>
<style>
.list {
	 padding: 0;
	 border-radius: 4px;
	 border: 1px solid #e0e0e0;
}
 .errors {
	 padding: 0;
	 color: red;
}

</style>