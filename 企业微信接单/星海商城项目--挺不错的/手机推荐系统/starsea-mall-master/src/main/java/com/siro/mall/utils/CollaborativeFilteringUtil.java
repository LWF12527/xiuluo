package com.siro.mall.utils;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.neighborhood.NearestNUserNeighborhood;
import org.apache.mahout.cf.taste.impl.recommender.GenericUserBasedRecommender;
import org.apache.mahout.cf.taste.impl.similarity.PearsonCorrelationSimilarity;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.neighborhood.UserNeighborhood;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.recommender.UserBasedRecommender;
import org.apache.mahout.cf.taste.similarity.UserSimilarity;

import java.io.File;
import java.io.IOException;
import java.util.List;

/**
 * @author luozhangheng
 * @version 1.0
 * @date 2024/2/1-23:44
 * @description 协同过滤混合推荐工具类
 */
public class CollaborativeFilteringUtil {

    private UserBasedRecommender recommender;

    public CollaborativeFilteringUtil(String dataModelFilePath) {
        try {
            // 从文件加载数据模型
            DataModel dataModel = new FileDataModel(new File(dataModelFilePath));

            // 定义用户相似度计算方法
            UserSimilarity similarity = new PearsonCorrelationSimilarity(dataModel);

            // 定义用户邻域，这里使用最近的N个用户
            UserNeighborhood neighborhood = new NearestNUserNeighborhood(2, similarity, dataModel);

            // 创建基于用户的协同过滤推荐器
            recommender = new GenericUserBasedRecommender(dataModel, neighborhood, similarity);
        } catch (IOException | TasteException e) {
            e.printStackTrace();
        }
    }

    // 获取给定用户的推荐物品
    public List<RecommendedItem> getRecommendations(long userID, int numberOfItems) {
        try {
            return recommender.recommend(userID, numberOfItems);
        } catch (TasteException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void main(String[] args) {
        // 示例用法
        String dataModelFilePath = "path/to/your/data.csv"; // 替换为实际数据文件路径
        CollaborativeFilteringUtil filteringUtil = new CollaborativeFilteringUtil(dataModelFilePath);

        long userId = 1; // 替换为实际用户ID
        int numberOfItems = 5; // 替换为想要推荐的物品数量

        List<RecommendedItem> recommendations = filteringUtil.getRecommendations(userId, numberOfItems);

        // 打印推荐结果
        if (recommendations != null) {
            for (RecommendedItem recommendation : recommendations) {
                System.out.println("Item ID: " + recommendation.getItemID() + ", Score: " + recommendation.getValue());
            }
        }
    }
}
