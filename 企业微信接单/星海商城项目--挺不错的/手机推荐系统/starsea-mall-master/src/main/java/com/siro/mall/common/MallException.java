package com.siro.mall.common;

/**
 * 异常处理类
 * @author starsea
 * @date 2024-01-22
 */
public class MallException extends RuntimeException {

    public MallException() {
    }

    public MallException(String message) {
        super(message);
    }

    /**
     * 丢出一台异常
     * @param message
     */
    public static void fail(String message) {
        throw new MallException(message);
    }
}
