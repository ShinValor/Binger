<template>
  <div>
    <ul v-show="errors.length > 0" class="errors">
      <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
    </ul>
    <div v-show="!errors.length">
      <h3>{{ list.name }}</h3>
      <!-- <p v-show="loading">Loading...</p> -->
      <ul class="list">
        <FavoriteMovieCell v-for="item in list" :key="item.title" :item="item" />
      </ul>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
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
    this.list = JSON.parse(`[{
		"popularity": 96.788,
		"vote_count": 579,
		"video": false,
		"poster_path": "https://image.tmdb.org/t/p/w500/tI8ocADh22GtQFV28vGHaBZVb0U.jpg",
		"id": 475430,
		"adult": false,
		"backdrop_path": "https://image.tmdb.org/t/p/w500/o0F8xAt8YuEm5mEZviX5pEFC12y.jpg",
		"original_language": "en",
		"original_title": "Artemis Fowl",
		"genres": [
			"Adventure",
			"Fantasy",
			"Science Fiction",
			"Family"
		],
		"title": "Artemis Fowl",
		"vote_average": 5.9,
		"overview": "Artemis Fowl is a 12-year-old genius and descendant of a long line of criminal masterminds. He soon finds himself in an epic battle against a race of powerful underground fairies who may be behind his father's disappearance.",
		"release_date": "2020-06-12"
	},
	{
		"popularity": 90.423,
		"vote_count": 9998,
		"video": false,
		"poster_path": "https://image.tmdb.org/t/p/w500/xT98tLqatZPQApyRmlPL12LtiWp.jpg",
		"id": 122917,
		"adult": false,
		"backdrop_path": "https://image.tmdb.org/t/p/w500/bVmSXNgH1gpHYTDyF9Q826YwJT5.jpg",
		"original_language": "en",
		"original_title": "The Hobbit: The Battle of the Five Armies",
		"genres": [
			"Action",
			"Adventure",
			"Fantasy"
		],
		"title": "The Hobbit: The Battle of the Five Armies",
		"vote_average": 7.3,
		"overview": "Immediately after the events of The Desolation of Smaug, Bilbo and the dwarves try to defend Erebor's mountain of treasure from others who claim it: the men of the ruined Laketown and the elves of Mirkwood. Meanwhile an army of Orcs led by Azog the Defiler is marching on Erebor, fueled by the rise of the dark lord Sauron. Dwarves, elves and men must unite, and the hope for Middle-Earth falls into Bilbo's hands.",
		"release_date": "2014-12-10"
	}, {
		"popularity": 84.838,
		"vote_count": 4979,
		"video": false,
		"poster_path": "https://image.tmdb.org/t/p/w500/aQvJ5WPzZgYVDrxLX4R6cLJCEaQ.jpg",
		"id": 454626,
		"adult": false,
		"backdrop_path": "https://image.tmdb.org/t/p/w500/stmYfCUGd8Iy6kAMBr6AmWqx8Bq.jpg",
		"original_language": "en",
		"original_title": "Sonic the Hedgehog",
		"genres": [
			"Action",
			"Comedy",
			"Science Fiction",
			"Family"
		],
		"title": "Sonic the Hedgehog",
		"vote_average": 7.5,
		"overview": "Based on the global blockbuster videogame franchise from Sega, Sonic the Hedgehog tells the story of the world’s speediest hedgehog as he embraces his new home on Earth. In this live-action adventure comedy, Sonic and his new best friend team up to defend the planet from the evil genius Dr. Robotnik and his plans for world domination.",
		"release_date": "2020-02-12"
	}
]`);
    // {
    //   axios
    //     .get(
    //       "http://localhost:5000/test"
    //     )
    //     .then(response => {
    //         console.log( response.data)
    //       this.list = response.data;
    //     });
    // }
  },
  mounted() {
    console.log(typeof this.list);
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