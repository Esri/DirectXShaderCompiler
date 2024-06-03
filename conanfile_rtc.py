from conans import ConanFile

class DirectXShaderCompilerConan(ConanFile):
    name = "DirectXShaderCompiler"
    version = "0.0.1"
    url = "https://github.com/duncanthomson/DirectXShaderCompiler"
    license = "https://github.com/duncanthomson/DirectXShaderCompiler/blob/main/LICENSE.TXT"
    description = "A compiler and related tools used to compile High-Level Shader Language (HLSL) programs into DirectX Intermediate Language (DXIL) representation"

    # RTC specific triple
    settings = "platform_architecture_target"

    def package(self):
        base = self.source_folder
        relative = "3rdparty/DirectXShaderCompiler"

        # headers
        self.copy("*.h", src=base + "/include/dxc", dst=relative + "/include/dxc")
        self.copy("*.hpp", src=base + "/include/dxc", dst=relative + "/include/dxc")

        # libraries
        # Only headers are required by RTC, at present: no library
