class Vaultx < Formula
  desc "Comprehensive Vault Cluster Status Checker"
  homepage "https://github.com/zbaban/vaultx"
  url "https://github.com/zbaban/vaultx/archive/v1.0.0.tar.gz"
  sha256 "replace_with_actual_sha256_after_first_release"
  license "MIT"

  depends_on "vault"
  depends_on "jq"

  def install
    bin.install "vaultx"
  end

  test do
    assert_match "Usage: vaultx", shell_output("#{bin}/vaultx --help")
  end
end
