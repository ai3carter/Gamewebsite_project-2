// Plot the default route once the page loads
var defaultURL = "/theme_count";
d3.json(defaultURL).then(function(data) {
  var data = [data];
  var layout = {
    margin: { t: 50, b: 100 },
    title: "Highest number games by theme",
    xaxis:{ticks:'Theme'},
    yaxis:{ticks:'Count'}
  };
  Plotly.plot("bar", data, layout);
});
d3.json("/genre_rating").then(function(data) {
  var data = [data1];
  var layout = {
    margin: { t: 50, b: 100 },
    title: "Top rated games by genre",
    xaxis:{ticks:'Genre'},
    yaxis:{ticks:'Score'}
  };
  Plotly.plot("bar", data, layout);
});

d3.json("/similar_games").then(function(data){
  var data=[data2];
  var layout={
    title:{text:"Top 100 games associated with similar games"}
    // showlegend: false,
    // height: 400,
    // width: 480
  };
  Plotly.plot('bar',data,layout);
    });

    
// Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("bar", "x", [newdata.x]);
  Plotly.restyle("bar", "y", [newdata.y]);
}
// Get new data whenever the dropdown selection changes
// in here, we dont have to set up the defaulturl for emoji_id & emoji name
// cuz back in index.html, there's onchange='getData(this.value)' pass in this three values
function getData(route) {
  console.log(route);
  d3.json(`/${route}`).then(function(data) {
    console.log("newdata", data);
    updatePlotly(data);
  });
}