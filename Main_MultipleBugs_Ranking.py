from util.FileManager import join_path
from ranking.MultipleBugsManager import multiple_bugs_ranking
from ranking.Spectrum_Expression import JACCARD, SORENSEN_DICE, TARANTULA, OCHIAI, OP2, BARINEL, DSTAR, ROGERS_TANIMOTO, \
    AMPLE, \
    SIMPLE_MATCHING, RUSSELL_RAO, COHEN, SCOTT, ROGOT1, GEOMETRIC_MEAN, M2, WONG1, SOKAL, DICE, HUMANN, ZOLTAR, \
    WONG2, ROGOT2, EUCLID, HAMMING, FLEISS, ANDERBERG, KULCZYNSKI2, HARMONIC_MEAN, GOODMAN

if __name__ == "__main__":
    # parameter configuration
    data_base_dir = "/Users/thu-trangnguyen/Documents/Research/SPL/"
    system_name = "Debug"
    bug_folder = "1Bug"
    w = 0.2
    kwise = "4wise"
    coverage_versions = [""]
    sbfl_metrics = [TARANTULA, OCHIAI, OP2, BARINEL, DSTAR,
                    RUSSELL_RAO, SIMPLE_MATCHING, ROGERS_TANIMOTO, AMPLE, JACCARD,
                    COHEN, SCOTT, ROGOT1, GEOMETRIC_MEAN, M2,
                    WONG1, SOKAL, SORENSEN_DICE, DICE, HUMANN,
                    WONG2, EUCLID, ZOLTAR,
                    ROGOT2, HAMMING, FLEISS, ANDERBERG,
                    GOODMAN, HARMONIC_MEAN, KULCZYNSKI2]
    # -----------------------
    system_dir = join_path(data_base_dir, system_name)
    bug_folder_dir = join_path(system_dir, bug_folder)
    multiple_bugs_ranking(system_name, bug_folder, bug_folder_dir, kwise, sbfl_metrics,
                          filtering_coverage_rate=0.0, coverage_version="", alpha=w)
