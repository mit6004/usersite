#include <stdio.h>
#define LSIZE 2000

int main(int argc,char **argv) {
  char line[LSIZE];
  int pnum = 0;
  int ppnum = 0;

  fprintf(stdout,"\
<html>\n\
<script language=\"JavaScript1.2\" src=\"tutprobs.js\"></script>\n\
<body background=\"../tile.gif\">\n\
<table width=\"630\" cellpadding=4><tr><td>\n\n\
<noscript>\n\
<table width=\"100%\" border=\"1\" cellpadding=\"8\" bgcolor=\"yellow\">\n\
<tr><td>\n\
You need to have Javascript enabled to view this page\n\
properly.  If your browser does not support Javascript\n\
or you have chosen not to enable it, please return to\n\
the previous page and use the appropriate link to view\n\
PDF versions of this tutorial page.\n\
</td></tr></table><p>\n\
</noscript>\n\n\
<div id=\"start\" class=question>\n\
<a href=\"#\" onClick=\"showall(); return false\"><img border=0 src=\"showall.gif\"></a>\n\
&nbsp;\n\
<a href=\"#\" onClick=\"initialize(); return false\"><img border=0 src=\"hideall.gif\"></a>\n\
<p>
");

  while (fgets(line,LSIZE,stdin) == line) {
    if (strcmp(line,"{question}\n") == 0) {
      if (ppnum > 0) fprintf(stdout,"</font></ul>");
      else fprintf(stdout,"<p>");
      fputs("</div>\n\n",stdout);
      pnum += 1;
      ppnum = 0;
      fprintf(stdout,"<div id=\"question%d\" class=question>\n<p><hr><p><u>Problem %d.</u>\n",pnum,pnum);
    } else if (strcmp(line,"{subquestion}\n") == 0) {
      if (ppnum > 0) fprintf(stdout,"</font></ul>");
      else fprintf(stdout,"<p>");
      ppnum += 1;
      fprintf(stdout,"</div>\n\n<div id=\"question%d%c\" class=question><ol type=\"A\" start=\"%d\"><li>\n",
	      pnum,'@'+ppnum,ppnum);
    } else if (strcmp(line,"{answer}\n") == 0) {
      fprintf(stdout,"</ol></div>\n\n<div id=\"control%d%c\" class=control><ul>\n<a href=\"#\" onClick=\"toggle('%d%c'); return false\"><img name=\"ctl\" src=\"show.gif\" border=0></a></ul></div>\n\n<div id=\"answer%d%c\" class=answer><ul><font color=\"blue\">\n",
	      pnum,'@'+ppnum,pnum,'@'+ppnum,pnum,'@'+ppnum);
    } else fputs(line,stdout);
  }

  if (ppnum >= 0) fprintf(stdout,"</i></ul>");
  else fprintf(stdout,"<p>");
  fprintf(stdout,"\
</div>\n\n\
<script language=\"JavaScript1.2\">initialize();</script>\n\
</td></tr></table>\n\
</body>\n\
</html>\n\
");

  exit(0);
}











