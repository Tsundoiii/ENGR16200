{
  description = "ENGR16200 development environment";

  inputs.nixpkgs.url = "nixpkgs";

  outputs =
    { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          (python3.withPackages (
            python-pkgs: with python-pkgs; [
              numpy
              matplotlib
            ]
          ))

          remmina
        ];
      };
    };
}
