from loguru import logger
import zipfile
import traceback
import json


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
    except Exception:
        logger.error(f"解压失败：未知错误\n{traceback.format_exc()}")
        return False

def APPInfo(path):
    """
    读取 APPInfo.json 中的内容
    :param path: APPInfo.json 文件目录
    :return: 读取成功时返回 data，失败时返回 None
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        print("✓ 文件读取成功")
        return data

    except FileNotFoundError:
        print(f"找不到位于{path}的JSON文件")
    except json.JSONDecodeError:
        print(f"JSON解析错误")
        return None
    except Exception as e:
        print(f"读取文件时出错，因为 {e}")
        return None



# unzip("../core1.py", "../cache")