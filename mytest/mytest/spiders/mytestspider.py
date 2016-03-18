#coding=utf-8
#!/usr/bin/env python
import scrapy
from mytest.items import MytestItem
from scrapy import Selector
doc='''
<li class="gl-item">
<div data-i="1" data-sku_temp="1861098" class="gl-i-wrap j-sku-item" data-sku="1861098" venderid="0" jdzy_shop_id="0">
    <div class="p-img">
        <a target="_blank" href="http://item.jd.com/1861098.html">
            <img title="打白条 12期或24期分期，返81减80元白条满减券（免息用户除外）" data-img="1" src="//img13.360buyimg.com/n7/jfs/t2302/16/135479564/94882/c76da045/55f0e877N3c24faa3.jpg" width="220" height="220"></a>
    </div>
    <div class="p-scroll">
        <span class="ps-prev">&lt; </span>
        <span class="ps-next">&gt;</span>
        <div class="ps-wrap">
            <ul class="ps-main">
                <li class="ps-item" ids="">
                <a title="玫瑰金" href="javascript:;">
                    <img data-sku="1861098" class="loading-style2" src="//img13.360buyimg.com/n9/jfs/t2302/16/135479564/94882/c76da045/55f0e877N3c24faa3.jpg" width="25" height="25"></a>
                </li>
                <li class="ps-item" ids="" ids_temp=""> 
                <a title="金色" href="javascript:;">
                    <img src="//img10.360buyimg.com/n9/jfs/t1750/64/1543556998/95929/2dd7e965/55f0e824Neac4417f.jpg" style="" data-sku="1861095" data-lazy-img="done" class="" width="25" height="25"></a>
                </li>
                <li class="ps-item" ids="" ids_temp=""> 
                <a title="银色" href="javascript:;">
                    <img src="//img11.360buyimg.com/n9/jfs/t2491/330/130347277/93583/10ac6d51/55f0e840N6609b12b.jpg" style="" data-sku="1861096" data-lazy-img="done" class="" width="25" height="25"></a>
                </li>
                <li class="ps-item" ids="" ids_temp=""> 
                <a title="深空灰" href="javascript:;">
                    <img src="//img12.360buyimg.com/n9/jfs/t2278/69/129833021/96430/df8863b1/55f0e861Nf585867f.jpg" style="" data-sku="1861097" data-lazy-img="done" class="" width="25" height="25">
                </a>
                </li>
            </ul>
        </div>
    </div>
    <div class="p-price">
        <strong class="J_price">
            <em>¥</em>
            <i>6388.00</i>
        </strong>
        <div class="p-icons J-pro-icons">
            <i class="goods-icons-s1" title="该商品支持货到付款">货到付款</i>
        </div>
    </div>
    <div class="p-name">
        <a target="_blank" title="打白条 12期或24期分期，返81减80元白条满减券（免息用户除外）" href="http://item.jd.com/1861098.html">
            <em>Apple iPhone 6s Plus (A1699) 64G 玫瑰金色 移动联通电信4G手机</em>
            <i class="promo-words">打白条 12期或24期分期，返81减80元白条满减券（免息用户除外）</i>
        </a>
    </div>
    <div class="p-commit">
        <strong>已有
            <a target="_blank" href="http://item.jd.com/1861098.html#comment">47722</a>人评价</strong>
    </div>
    <div class="p-focus">
        <a class="J_focus" data-sku="1861098" href="javascript:;">
            <i></i>关注</a>
    </div>
    <div class="p-shop" data-score="4" data-reputation="0" data-shopid="" data-shop_name="" data-done="1"></div>
    <div data-stock_h="33" data-stock_v="1" class="p-stock" data-isdeliveryable="5" style="display: none"></div>
</div>
</li>
'''

class mytestspider(scrapy.Spider):
    name='mytest'
    start_urls=['http://list.jd.com/list.html?cat=9987%2C653%2C655&go=0']
    def parse(self,response):
        item=MytestItem()
        for sel in response.xpath('//li[@class="gl-item"]/div[@class="gl-i-wrap j-sku-item"]'):
            item['link']=sel.xpath('div[@class="p-name"]/a/@href').extract()
            item['title']=sel.xpath('div[@class="p-name"]/a/em/text()').extract()
            item['price']=sel.xpath('div[@class="p-price"]/strong/i/text()').extract()
            item['comment']=sel.xpath('div[@class="p-commit"]/strong/a/text()').extract()
            yield item









