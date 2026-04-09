from loguru import logger
import zipfile
import traceback


def unzip(path, outputPath):
    """
    解压缩文件
    :param path: 压缩文件位置
    :param outputPath: 输出目录
    :return: bool: True：成功；False：失败
    """
    logger.info(f"解压文件 {path} 到 {outputPath}")

    try:
        with zipfile.ZipFile(path, 'r') as zip_ref:
            logger.info("正在解压")
            zip_ref.extractall(outputPath)
            logger.info("解压成功")
            return True
    except FileNotFoundError:
        logger.error(f"解压失败：位于 {path} 的压缩文件不存在\n{traceback.format_exc()}")
        return False
    except zipfile.BadZipFile:
        logger.error(f"解压失败：压缩文件损坏或不是有效的ZIP文件 - {path}\n{traceback.format_exc()}")
        return False
    except Exception as e:
        logger.error(f"解压失败：未知错误\n{traceback.format_exc()}")
        return False

# unzip("../core1.py", "../cache")