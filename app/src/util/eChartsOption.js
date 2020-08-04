// import store from "../store/index";

export const eChartsOption = {
  title: {
    text: "Movie Dashboard",
    subtext: "Most Liked Movie Genres",
    left: "center",
    textStyle: {
      color: "white"
    }
  },
  tooltip: {
    trigger: "item",
    formatter: "{a} <br/>{b} : {c} ({d}%)"
  },
  legend: {
    left: "center",
    top: "bottom",
    data: [
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
    textStyle: {
      color: "white"
    }
  },
  series: [
    {
      name: "You",
      type: "pie",
      radius: [30, 200],
      center: ["50%", "50%"],
      roseType: "area",
      data: []
      // data: store.getters.genres
    }
  ]
};
