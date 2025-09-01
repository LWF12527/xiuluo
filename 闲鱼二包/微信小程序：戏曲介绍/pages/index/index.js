// index.js
Page({
  onLoad(options) {
  },
  gointro: function(e){
    var id = e.currentTarget.dataset.id;
    wx.navigateTo({
      url: '../intro/intro?id='+id,
    })
  }
})
