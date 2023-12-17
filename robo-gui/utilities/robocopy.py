"""Module builds a robocopy command"""
import pathlib


class Robocopy:
    """RobocopyCommandBuilder class"""

    def __init__(
        self,
    ):
        """initializes the RobocopyCommandBuilder class"""

        # self.arguments = self.__set_robocopy_arguments__()

    def get_arguments(self):
        """returns the robocopy arguments"""
        return self.arguments


def get_robocopy_arguments():
    """sets the robocopy options"""
    arguments = {
        "/s": "Copies subdirectories but not empty ones",
        "/e": "Copies subdirectories including empty ones",
        "/z": "Copies files in restartable mode",
        "/b": "Copies files in backup mode",
        "/zb": "Uses restartable mode, but if access is denied, switches to backup mode",
        "/j": "Copies using unbuffered I/O",
        "/efsraw": "Copies all encrypted files in EFS RAW mode",
        "/sec": "Copies files with security",
        "/copyall": "Copies all file information",
        "/nocopy": "Copies no file information; useful with /purge",
        "/secfix": "Fixes file security on all files, even skipped ones",
        "/timfix": "Fixes file times on all files, even skipped ones",
        "/purge": "Deletes destination files no longer in the source",
        "/mir": "Mirrors a directory tree",
        "/mov": "Moves files and deletes from the source after copying",
        "/move": "Moves files and directories and deletes from the source after copying",
        "/create": "Creates a directory tree and zero-length files only",
        "/fat": "Creates files with 8.3 character-length FAT file names only",
        "/256": "Turns off support for paths longer than 256 characters",
        "/a": "Copies only files with the Archive attribute set",
        "/m": "Copies only files with the Archive attribute and resets it",
        "/xc": "Excludes changed files",
        "/xn": "Excludes newer files",
        "/xo": "Excludes older files",
        "/xx": "Excludes extra files and directories",
        "/xl": "Excludes 'lonely' files and directories",
        "/is": "Includes the same files",
        "/it": "Includes 'tweaked' files",
        "/xj": "Excludes junction points",
        "/fft": "Assumes FAT file times",
        "/dst": "Compensates for DST time differences",
        "/xjd": "Excludes junction points for directories",
        "/xjf": "Excludes junction points for files",
        "/reg": "Saves options to the registry",
        "/l": "Lists only, no copying",
        "/x": "Reports all extra files",
        "/v": "Produces verbose output",
        "/ts": "Includes file timestamps in logs",
        "/fp": "Includes full path names in logs",
        "/bytes": "Prints sizes in bytes",
        "/ns": "Omits file size logging",
        "/nc": "Omits class logging",
        "/nfl": "Omits file names from logging",
        "/ndl": "Omits directory names from logging",
        "/np": "Omits progress display",
        "/eta": "Shows estimated time of arrival of copied files",
        "/njh": "No job header",
        "/njs": "No job summary",
        "/unicode": "Displays status output as Unicode",
        "/quit": "Quits after processing command line",
        "/nosd": "No source directory is specified",
        "/nodd": "No destination directory is specified",
    }
    return arguments
