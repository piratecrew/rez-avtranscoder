CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(avtranscoder_version ${AVTRANSCODER_VERSION})

set(url_avtranscoder https://github.com/avTranscoder/avTranscoder.git)
set(tag_avtranscoder v${avtranscoder_version})


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    avtranscoder
    GIT_REPOSITORY ${url_avtranscoder}
    GIT_TAG ${tag_avtranscoder}
    PREFIX avtranscoder
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DCMAKE_PREFIX_PATH=$ENV{REZ_FFMPEG_ROOT}
    BUILD_COMMAND make
    INSTALL_COMMAND ${install_cmd}
)

rez_install_files(
    cmake/avtranscoder.cmake
    DESTINATION .
)
