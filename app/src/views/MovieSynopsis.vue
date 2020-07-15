<template>
  <a-layout>
    <MovieOverview
      :key="this.$route.params.id + 'Synopsis'"
      :movieID="parseInt(this.$route.params.id)"
    />
    <MovieSynopsisMovieList
      listType="Movie Recommendations"
      :movieID="parseInt(this.$route.params.id)"
      :key="this.$route.params.id + 'Recommendation'"
    />
    <MovieSynopsisMovieList
      listType="Similar Movies"
      :movieID="parseInt(this.$route.params.id)"
      :key="this.$route.params.id + 'Similiar'"
    />
    <MovieSynopsisCastList
      :key="this.$route.params.id + 'CastList'"
      :movieID="parseInt(this.$route.params.id)"
    />
  </a-layout>
</template>

<script>
import MovieSynopsisMovieList from "@/components/MovieSynopsisMovieList.vue";
import MovieSynopsisCastList from "@/components/MovieSynopsisCastList.vue";
import MovieOverview from "@/components/MovieOverview.vue";

export default {
  name: "MovieSynopsis",
  components: {
    MovieOverview,
    MovieSynopsisMovieList,
    MovieSynopsisCastList
  }
};
</script>

<style scoped>
.left-align {
  text-align: left;
}

.header {
  display: flex;
  flex-wrap: nowrap;
  background-color: rgba(0, 34, 95, 0.7);
  background-blend-mode: multiply;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  padding-bottom: 4rem !important;
  padding-top: 4.5rem !important;
}

.header-contents {
  display: flex;
  flex-wrap: nowrap;
  margin: 2em;
}

.poster-wrapper {
  display: block;
  min-width: 300px;
  width: 300px;
  height: 450px;
  position: relative;
  top: 0;
  left: 0;
}

.poster {
  display: block;
  width: 100%;
  min-width: 100%;
  height: 100%;
  min-height: 100%;
  border-width: 0px;
  outline: none;
}

.movie-info-part {
  display: flex;
}

.movie-info {
  padding-left: 40px;
}

.key-info {
  width: 100%;
  margin-bottom: 24px;
}

.movie-title {
  margin: 0;
  padding: 0;
  font-size: 2.2rem;
  font-weight: 700;
  display: inline;
}

.tagline {
  margin: 0;
  padding: 0;
  font-weight: 350;
  font-size: 1.3rem;
  font-style: italic;
  opacity: 0.7;
  display: inline;
}

.general-info {
  display: flex;
}

.release-date,
.genres,
.runtime {
  padding-left: 20px;
  position: relative;
  top: 0;
  left: 0;
}

.score-section {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  height: 68px;
  margin-right: 20px;
}

.movie-score {
  font-size: 30px;
  font-weight: 600;
}

.score-section-text {
  font-weight: 700;
  margin-left: 6px;
  white-space: pre-line;
  font-size: 14px;
}

.movie-overview-text {
  text-align: left;
}

.text-overview {
  font-weight: 600;
  font-size: 1.3em;
}

.fontColor {
  color: ivory;
}

@media only screen and (max-width: 600px) {
  .header-contents,
  .tagline,
  .movie-title {
    display: block;
  }

  .tagline {
    margin-top: -10px;
    padding-left: 15px;
  }

  .title-wrapper {
    margin-bottom: 10px;
  }

  .general-info {
    text-align: left;
  }

  .release-date {
    padding-left: 0px;
  }

  .poster-wrapper {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
