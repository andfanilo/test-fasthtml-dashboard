console.log("Hello Echarts");

var myChart = echarts.init(document.getElementById("chart"));

var option = {
  title: {
    text: "Views in Millions",
  },
  tooltip: {},
  legend: {
    data: ["views"],
  },
  xAxis: {
    data: ["2020", "2021", "2022", "2023", "2024"],
  },
  yAxis: {},
  series: [
    {
      data: [10, 22, 28, 37, 41],
      type: "line",
      lineStyle: {
        normal: {
          color: "red",
          width: 4,
          type: "dashed",
        },
      },
    },
  ],
};

myChart.setOption(option);
