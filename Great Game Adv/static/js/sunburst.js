var data = [{
    type: "sunburst",
    labels: ["Root", "The Legend of Zelda","The Legend of Zelda: Breath of the Wild","Grand Theft Auto", "Grand Theft Auto: San Andreas", "Grand Theft Auto: Vice City", "Pokemon", "Pokemon Sword", "Pokemon Shield", "Pokemon Masters", "Tom Clancy", "Tom Clancy's The Division 2", "Tom Clancy's Ghost Recon: Wildlands"],
    parents: ["", "Root", "The Legend of Zelda", "Root", "Grand Theft Auto", "Grand Theft Auto", "Root", "Pokemon", "Pokemon", "Pokemon","Root", "Tom Clancy", "Tom Clancy", "Root"],
    values:  [0, 96, 95, 91, 91, 75, 76, 75, 73, 26, 86, 85, 73],
    outsidetextfont: {size: 20, color: "#377eb8"},
    leaf: {opacity: 0.4},
    marker: {line: {width: 2}},
  }];
  
  var layout = {
    margin: {l: 0, r: 0, b: 0, t: 0},
    width: 500,
    height: 500
  };
  

  Plotly.newPlot('myDiv', data, layout, {showSendToCloud:true});


