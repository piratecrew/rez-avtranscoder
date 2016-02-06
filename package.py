name = "avtranscoder"

version = "0.8.1"

description = \
    """
    avTranscoder
    C++ API for Libav / FFmpeg
    """

variants = [
    ["platform-linux"]
]

requires = [
    "python",
    "ffmpeg"
]

uuid = "repository.avtranscoder"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
