<template>
  <div class="search">
    <div class="search-bar collapsible"   >
      <a-input-search
        placeholder="Search Movies"
        v-model="movieQuery"
        enter-button
        @search="onTitleSearch"
        :disabled="collapse"
      >
        <a-icon slot="prefix" type="menu"  @click="toggle" :class="collapse ? 'active' : '' "/>
      </a-input-search>
    </div>
    <div class="genre-tags content" :class="collapse ? 'open-collapsable' : 'close-collapsable' ">
      <h4 class="genre-search-title">Genres</h4>
      <template v-for="tag in Genres">
        <a-checkable-tag
          :key="tag"
          :checked="selectedTags.indexOf(tag) > -1"
          @change="checked => handleChange(tag, checked)"
        >
          {{ tag }}
        </a-checkable-tag>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  props: {
    movieQuery: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      collapse: false,
      searchResults: Array,
      Genres: [
        "Adventure",
        "Fantasy",
        "Animation",
        "Drama",
        "Horror",
        "Action",
        "Comedy",
        "History",
        "Western",
        "Thriller",
        "Crime",
        "Documentary",
        "Science Fiction",
        "Mystery",
        "Music",
        "Romance",
        "Family",
        "War",
        "Action & Adventure",
        "Sci-Fi & Fantasy",
        "TV Movie"
      ],
      selectedTags: []
    };
  },
  created() {
    if (this.$route.query.with_genres) {
      console.log(this.$route.query.with_genres);
      const nextSelectedTags = [...this.selectedTags, this.$route.query.with_genres];
      this.selectedTags = nextSelectedTags;
      this.toggle();
      // document.getElementsByClassName("collapsible")[0].nextElementSibling.style.display = "block";
      // document.getElementsByClassName("collapsible")[0].classList.toggle("active");
    }
  },
  mounter(){this.toggle();},
  methods: {
    toggle() {
      // var coll = document.getElementsByClassName("collapsible")[0];
      // coll.addEventListener("click", function() {
      //   coll.classList.toggle("active");
      //   var content = coll.nextElementSibling;
      //   if (content.style.display === "block") {
      //     content.style.display = "none";
      //   } else {
      //     content.style.display = "block";
      //   }
      // });
      this.collapse = !this.collapse;
    },
    onTitleSearch() {
      this.$router.push({
        name: "Search",
        query: { movieQuery: this.movieQuery }
      });
    },
    onGenreSearch() {
      this.$router.push({
        name: "Search",
        query: { with_genres: this.genres }
      });
    },
    handleChange(tag, checked) {
      const { selectedTags } = this;
      const nextSelectedTags = checked
        ? [...selectedTags, tag]
        : selectedTags.filter(t => t !== tag);
      this.selectedTags = nextSelectedTags;
      this.onGenreSearch();
    }
  },
  computed: {
    genres: function() {
      return this.selectedTags.join(",");
    }
  }
};
</script>

<style scoped>
/* .search-bar {
  width: 50%;
  margin: 50px auto 25px;
} */

@media screen and (max-width: 500px) {
  /* applies styles to any device screen sizes below 800px wide */

  /* .search-bar {
    width: 75%;
    margin: 15px auto;
  } */
}
.search {
  width: 75%;
  align-content: center;
  align-items: center;
  margin: 15px auto;
}
.genre-tags {
  background-color: aqua;
}

.collapsible {
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.content {
  display: none;
  overflow: hidden;
  background-color: rgb(238, 241, 246);
  width: 75%;
  margin-left: 18px;
}
.genre-search-title {
  text-align: left;
  padding-top: 1.5rem;
  padding-left: 1.5rem;
  padding-bottom: 1rem;
}
.ant-tag {
  padding: 5px;
  margin: 2px;
  /* border: 1px solid #001529; */
  border-left: 3px solid gold;
  background-color: white;
}
.ant-tag-checkable-checked {
  color: #fff;
  background-color: #1890ff;
  background-color: gb(0, 21, 41);
}
.open-collapsable {
  display: block;
}
.close-collapsable {
  display: none;
}

</style>
