// import { store } from "../store/index";

export const eChartsOption = {
  title: {
    text: "Movie Dashboard",
    subtext: "Most Searched Movie Genres",
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
      data: [
        // { name: "Adventure", value: 0 },
        // { name: "Fantasy", value: 0 },
        // { name: "Animation", value: 0 },
        // { name: "Drama", value: 0 },
        // { name: "Horror", value: 0 },
        // { name: "Comedy", value: 0 },
        // { name: "History", value: 0 },
        // { name: "Western", value: 0 },
        // { name: "Thriller", value: 0 },
        // { name: "Crime", value: 0 },
        // { name: "Documentary", value: 0 },
        // { name: "Science Fiction", value: 0 },
        // { name: "Mystery", value: 0 },
        // { name: "Music", value: 0 },
        // { name: "Romance", value: 0 },
        // { name: "Family", value: 0 },
        // { name: "War", value: 0 },
        // { name: "Action & Adventure", value: 0 },
        // { name: "News", value: 0 },
        // { name: "Reality", value: 0 },
        // { name: "Sci-Fi & Fantasy", value: 0 },
        // { name: "Soaps", value: 0 },
        // { name: "Talk", value: 0 },
        // { name: "War & Politics", value: 0 },
        // { name: "TV Movie", value: 0 }
      ]
    }
  ]
};
