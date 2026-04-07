# 核心

import requests
import time
import logging
from pathlib import Path

# 配置日志
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 控制台处理器
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class internet:
    @staticmethod
    def download(url, savePath="./Download", speed=0):
        """
        下载文件
        Args:
            url: 下载链接
            savePath: 保存位置，如：C:\Download；默认./Download
            speed: 下载限速（KB/S）；默认0（不限速）
        Returns:
            bool: 下载成功返回True，失败返回False
        """
        # 创建保存目录
        save_dir = Path(savePath)
        save_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"保存目录已创建/确认: {save_dir.absolute()}")

        # 获取文件名
        filename = url.split('/')[-1].split('?')[0]
        if not filename:
            filename = "download_file"
            logger.warning(f"无法从URL解析文件名，使用默认名称: {filename}")

        filepath = save_dir / filename
        logger.info(f"开始从 {url} 下载文件 {filename} ，保存到 {filepath.absolute()}")

        if speed > 0:
            logger.info(f"下载限速: {speed} KB/s")
        else:
            logger.info("不限速下载")

        try:
            # 发送请求
            logger.debug("正在发送请求")
            response = requests.get(url, stream=True)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))
            if total_size > 0:
                logger.info(f"文件大小: {total_size / 1024:.2f} KB ({total_size / (1024*1024):.2f} MB)")
            else:
                logger.warning("无法获取文件大小")

            # 下载文件
            downloaded = 0
            start_time = time.time()
            last_log_time = start_time
            chunk_size = 8192

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)

                        # 限速
                        if speed > 0:
                            elapsed = time.time() - start_time
                            expected_time = downloaded / (speed * 1024)
                            if elapsed < expected_time:
                                time.sleep(expected_time - elapsed)

                        # 输出进度日志
                        current_time = time.time()
                        if current_time - last_log_time >= 1:
                            if total_size > 0:
                                progress = (downloaded / total_size) * 100
                                speed_bps = downloaded / (current_time - start_time) / 1024  # KB/s
                                logger.info(f"下载进度: {progress:.1f}% ({downloaded / 1024:.1f} KB / {total_size / 1024:.1f} KB) 速度: {speed_bps:.1f} KB/s")
                            else:
                                logger.info(f"已下载: {downloaded / 1024:.1f} KB")
                            last_log_time = current_time

            elapsed_time = time.time() - start_time
            avg_speed = downloaded / elapsed_time / 1024 if elapsed_time > 0 else 0

            logger.info(f"下载完成，文件名: {filename}, 大小: {downloaded / 1024:.2f} KB, 耗时: {elapsed_time:.2f}秒, 平均速度: {avg_speed:.2f} KB/s")
            return True

        except requests.exceptions.RequestException as e:
            logger.error(f"下载请求失败: {e}")
            # 删除不完整的文件
            if filepath.exists():
                filepath.unlink()
                logger.warning(f"已删除不完整的文件: {filepath}")
            return False
        except Exception as e:
            logger.exception(f"下载时发生未知错误: {e}")
            if filepath.exists():
                filepath.unlink()
                logger.warning(f"已删除不完整的文件: {filepath}")
            return False