<template>
  <div class="search">
    <a-tabs default-active-key="1" @change="callback">
      <a-tab-pane key="1" tab="Title Search">
        <a-input-search
          class="search-bar"
          placeholder="Search Movies"
          v-model="movieQuery"
          enter-button
          @search="onTitleSearch"
        />
      </a-tab-pane>
      <a-tab-pane key="2" tab="Genre Search">
        <div class="genre-tags">
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
      </a-tab-pane>
    </a-tabs>
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
        "Kids",
        "News",
        "Reality",
        "Sci-Fi & Fantasy",
        "Soaps",
        "Talk",
        "War & Politics",
        "TV Movie"
      ],
      selectedTags: []
    };
  },
  methods: {
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
  /* margin-bottom: 2.5rem; */
}
</style>
