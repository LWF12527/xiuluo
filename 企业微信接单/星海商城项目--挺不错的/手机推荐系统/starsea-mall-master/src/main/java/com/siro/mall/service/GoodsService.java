package com.siro.mall.service;

import com.siro.mall.entity.Goods;
import com.siro.mall.utils.PageQueryUtil;
import com.siro.mall.utils.PageResult;

import java.util.List;

/**
 * @author starsea
 * @date 2024-01-23
 */
public interface GoodsService {
    //后台分页
    PageResult getGoodsPage(PageQueryUtil pageUtil);

    //添加手机
    String saveGoods(Goods goods);

    //批量新增手机数据
    void batchSaveGoods(List<Goods> newBeeMallGoodsList);

    //修改手机信息
    String updateGoods(Goods goods);

    //获取手机详情
    Goods getGoodsById(Long id);

    //批量修改销售状态(上架下架)
    Boolean batchUpdateSellStatus(Long[] ids,int sellStatus);

    //手机搜索
    PageResult searchGoods(PageQueryUtil pageUtil);
}
