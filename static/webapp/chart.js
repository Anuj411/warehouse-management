var lineArea, widgetlineChart, widgetlineChart1, widgetlineChart2, widgetlineChart3, stackbarchart, lineArea2, lineChart, barChart, donut;
$(window).on("load", function() {
    widgetlineChart = new Chartist.Line("#Widget-line-chart", {
        labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        series: [
            [50, 45, 60, 55, 70, 55, 60, 55, 65, 57]
        ]
    }, {
        axisX: {
            showGrid: !0,
            showLabel: !1,
            offset: 0
        },
        axisY: {
            showGrid: !1,
            low: 40,
            showLabel: !1,
            offset: 0
        },
        lineSmooth: Chartist.Interpolation.cardinal({
            tension: 0
        }),
        fullWidth: !0
    }), widgetlineChart1 = new Chartist.Line("#Widget-line-chart1", {
        labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        series: [
            [80, 60, 70, 50, 60, 53, 71, 48, 65, 60]
        ]
    }, {
        axisX: {
            showGrid: !0,
            showLabel: !1,
            offset: 0
        },
        axisY: {
            showGrid: !1,
            low: 40,
            showLabel: !1,
            offset: 0
        },
        lineSmooth: Chartist.Interpolation.cardinal({
            tension: 0
        }),
        fullWidth: !0
    }), widgetlineChart2 = new Chartist.Line("#Widget-line-chart2", {
        labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        series: [
            [45, 55, 51, 65, 50, 62, 58, 70, 48, 57]
        ]
    }, {
        axisX: {
            showGrid: !0,
            showLabel: !1,
            offset: 0
        },
        axisY: {
            showGrid: !1,
            low: 40,
            showLabel: !1,
            offset: 0
        },
        lineSmooth: Chartist.Interpolation.cardinal({
            tension: 0
        }),
        fullWidth: !0
    }), widgetlineChart3 = new Chartist.Line("#Widget-line-chart3", {
        labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        series: [
            [70, 55, 90, 49, 65, 60, 78, 55, 80, 68]
        ]
    }, {
        axisX: {
            showGrid: !0,
            showLabel: !1,
            offset: 0
        },
        axisY: {
            showGrid: !1,
            low: 40,
            showLabel: !1,
            offset: 0
        },
        lineSmooth: Chartist.Interpolation.cardinal({
            tension: 0
        }),
        fullWidth: !0
    }), (lineArea = new Chartist.Line("#line-area", {
        labels: [1, 2, 3, 4, 5, 6, 7, 8],
        series: [
            [0, 20, 10, 45, 20, 36, 21, 0],
            [0, 5, 22, 14, 32, 12, 28, 0]
        ]
    }, {
        low: 0,
        showArea: !0,
        fullWidth: !0,
        onlyInteger: !0,
        axisY: {
            low: 0,
            scaleMinSpace: 50
        },
        axisX: {
            showGrid: !1
        }
    })).on("created", function(e) {
        var t = e.svg.elem("defs");
        t.elem("linearGradient", {
            id: "gradient",
            x1: 0,
            y1: 1,
            x2: 1,
            y2: 0
        }).elem("stop", {
            offset: 0,
            "stop-color": "rgba(0, 201, 255, 1)"
        }).parent().elem("stop", {
            offset: 1,
            "stop-color": "rgba(146, 254, 157, 1)"
        }), t.elem("linearGradient", {
            id: "gradient1",
            x1: 0,
            y1: 1,
            x2: 1,
            y2: 0
        }).elem("stop", {
            offset: 0,
            "stop-color": "rgba(132, 60, 247, 1)"
        }).parent().elem("stop", {
            offset: 1,
            "stop-color": "rgba(56, 184, 242, 1)"
        })
    }), (stackbarchart = new Chartist.Bar("#Stack-bar", {
        labels: label,
        series: [
            series_1,
            series_2
        ]
    }, {
        stackBars: !0,
        fullWidth: !0,
        axisX: {
            showGrid: !1
        },
        axisY: {
            showGrid: !1,
            showLabel: !1,
            offset: 0
        },
        chartPadding: 30
    })).on("created", function(e) {
        e.svg.elem("defs").elem("linearGradient", {
            id: "linear",
            x1: 0,
            y1: 1,
            x2: 0,
            y2: 0
        }).elem("stop", {
            offset: 0,
            "stop-color": "#7441DB"
        }).parent().elem("stop", {
            offset: 1,
            "stop-color": "#C89CFF"
        })
    }), stackbarchart.on("draw", function(e) {
        "bar" === e.type ? e.element.attr({
            style: "stroke-width: 5px",
            x1: e.x1 + .001
        }) : "label" === e.type && e.element.attr({
            y: 270
        })
    }), (lineArea2 = new Chartist.Line("#line-area2", {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        series: [
            [5, 30, 25, 55, 45, 65, 60, 105, 80, 110, 120, 150],
            [80, 95, 87, 155, 140, 147, 130, 180, 160, 175, 165, 200]
        ]
    }, {
        showArea: !0,
        fullWidth: !0,
        lineSmooth: Chartist.Interpolation.none(),
        axisX: {
            showGrid: !1
        },
        axisY: {
            low: 0,
            scaleMinSpace: 50
        }
    }, [
        ["screen and (max-width: 640px) and (min-width: 381px)", {
            axisX: {
                labelInterpolationFnc: function(e, t) {
                    return t % 2 == 0 ? e : null
                }
            }
        }],
        ["screen and (max-width: 380px)", {
            axisX: {
                labelInterpolationFnc: function(e, t) {
                    return t % 3 == 0 ? e : null
                }
            }
        }]
    ])).on("created", function(e) {
        var t = e.svg.elem("defs");
        t.elem("linearGradient", {
            id: "gradient2",
            x1: 0,
            y1: 1,
            x2: 0,
            y2: 0
        }).elem("stop", {
            offset: 0,
            "stop-opacity": "0.2",
            "stop-color": "transparent"
        }).parent().elem("stop", {
            offset: 1,
            "stop-opacity": "0.2",
            "stop-color": "#60AFF0"
        }), t.elem("linearGradient", {
            id: "gradient3",
            x1: 0,
            y1: 1,
            x2: 0,
            y2: 0
        }).elem("stop", {
            offset: .3,
            "stop-opacity": "0.2",
            "stop-color": "transparent"
        }).parent().elem("stop", {
            offset: 1,
            "stop-opacity": "0.2",
            "stop-color": "#6CD975"
        })
    }), lineArea2.on("draw", function(e) {
        if ("point" === e.type) {
            var t = new Chartist.Svg("circle", {
                cx: e.x,
                cy: e.y,
                r: 4,
                class: "ct-point-circle"
            });
            e.element.replace(t)
        } else if ("label" === e.type) {
            var a = e.width / 2 + (30 - e.width);
            e.element.attr({
                x: e.element.attr("x") - a
            })
        }
    }), (lineChart = new Chartist.Line("#lineChart", {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        series: [
            [80, 85, 75, 65, 63, 70, 82]
        ]
    }, {
        axisX: {
            showGrid: !1
        },
        axisY: {
            showGrid: !1,
            showLabel: !1,
            low: 0,
            high: 100,
            offset: 0
        },
        fullWidth: !0,
        offset: 0
    })).on("created", function(e) {
        if ("point" === e.type) {
            var t = new Chartist.Svg("circle", {
                cx: e.x,
                cy: e.y,
                r: 4,
                class: "ct-point-circle"
            });
            e.element.replace(t)
        } else if ("label" === e.type) {
            var a = e.width / 2 + (30 - e.width);
            e.element.attr({
                x: e.element.attr("x") - a
            })
        }
    }), (barChart = new Chartist.Bar("#bar-chart", {
        labels: ["Sport", "Music", "Travel", "News"],
        series: [
            [53, 23, 40, 30]
        ]
    }, {
        axisX: {
            showGrid: !1
        },
        axisY: {
            showGrid: !1,
            showLabel: !1,
            offset: 0
        },
        low: 0,
        high: 60
    }, [
        ["screen and (max-width: 640px)", {
            seriesBarDistance: 5,
            axisX: {
                labelInterpolationFnc: function(e) {
                    return e[0]
                }
            }
        }]
    ])).on("created", function(e) {
        var t = e.svg.elem("defs");
        t.elem("linearGradient", {
            id: "gradient4",
            x1: 0,
            y1: 1,
            x2: 0,
            y2: 0
        }).elem("stop", {
            offset: 0,
            "stop-color": "#8E1A38"
        }).parent().elem("stop", {
            offset: 1,
            "stop-color": "#FAA750"
        }), t.elem("linearGradient", {
            id: "gradient5",
            x1: 0,
            y1: 1,
            x2: 0,
            y2: 0
        }).elem("stop", {
            offset: 0,
            "stop-color": "#1750A5"
        }).parent().elem("stop", {
            offset: 1,
            "stop-color": "#40C057"
        }), t.elem("linearGradient", {
            id: "gradient6",
            x1: 0,
            y1: 1,
            x2: 0,
            y2: 0
        }).elem("stop", {
            offset: 0,
            "stop-color": "#3B1C93"
        }).parent().elem("stop", {
            offset: 1,
            "stop-color": "#60AFF0"
        }), t.elem("linearGradient", {
            id: "gradient7",
            x1: 0,
            y1: 1,
            x2: 0,
            y2: 0
        }).elem("stop", {
            offset: 0,
            "stop-color": "#562DB7"
        }).parent().elem("stop", {
            offset: 1,
            "stop-color": "#F55252"
        })
    }), barChart.on("draw", function(e) {
        "bar" === e.type && e.element.attr({
            y1: 195,
            x1: e.x1 + .001
        })
    });
    var t = {
        series: [{
            name: "done",
            className: "ct-done",
            value: 23
        }, {
            name: "progress",
            className: "ct-progress",
            value: 14
        }, {
            name: "outstanding",
            className: "ct-outstanding",
            value: 35
        }, {
            name: "started",
            className: "ct-started",
            value: 28
        }]
    };
    (donut = new Chartist.Pie("#donut-dashboard-chart", {
        series: [{
            name: "done",
            className: "ct-done",
            value: 23
        }, {
            name: "progress",
            className: "ct-progress",
            value: 14
        }, {
            name: "outstanding",
            className: "ct-outstanding",
            value: 35
        }, {
            name: "started",
            className: "ct-started",
            value: 28
        }]
    }, {
        donut: !0,
        startAngle: 0,
        labelInterpolationFnc: function(e) {
            return t.series.reduce(function(e, t) {
                return e + t.value
            }, 0) + "%"
        }
    })).on("draw", function(e) {
        "label" === e.type && (0 === e.index ? e.element.attr({
            dx: e.element.root().width() / 2,
            dy: e.element.root().height() / 2
        }) : e.element.remove())
    })
}), $(window).on("resize", function() {
    lineArea.update(), widgetlineChart.update(), widgetlineChart1.update(), widgetlineChart2.update(), widgetlineChart3.update(), stackbarchart.update(), lineArea2.update(), lineChart.update(), barChart.update(), donut.update()
});