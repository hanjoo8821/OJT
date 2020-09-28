package local.hanjoo;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.FileWriter;
import java.io.File;
import java.sql.*;

public class Dbms {

    private final Connection con;
    private String sql;

    public Dbms(Connection con) {
        this.con = con;
    }

    // Set -------------------------------------------------------------------------------------------------------------

    public void setSql(String sql) {
        this.sql = sql;
    }

    // Query  ----------------------------------------------------------------------------------------------------------
    public void showTable() {
        try {
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery(sql);

            try {
                ResultSetMetaData rsMd = rs.getMetaData();
                int numCols = rsMd.getColumnCount();

                while (rs.next()) {
                    for (int i = 1; i <= numCols; i++) {
                        if (rs.getString(i) == null) {
                            System.out.print(" ");
                        } else {
                            System.out.print(rs.getString(i) + " ");
                        }
                    }
                    System.out.println();
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                rs.close();
                st.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void showCol(String col) {
        try {
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery(sql);
            try {
                while (rs.next()) {
                    if (rs.getString(col) == null) {
                        System.out.print("null");
                    } else {
                        System.out.print(rs.getString(col));
                    }
                    System.out.print(" ");
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                rs.close();
                st.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Output  ----------------------------------------------------------------------------------------------------------
    public void outCol(String col) {
        try {
            String path = ".//Output";

            File Folder = new File(path);
            if (!Folder.exists()) {
                Folder.mkdir();
            }
            try {
                Statement st = con.createStatement();
                ResultSet rs = st.executeQuery(sql);

                BufferedWriter writer = new BufferedWriter(new FileWriter(path + "//" + col + ".txt"));
                try {
                    while (rs.next()) {
                        if (rs.getString(col) == null) {
                            writer.write("null");
                        } else {
                            writer.write(rs.getString(col));
                        }
                        writer.newLine();
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                } finally {
                    writer.close();
                    rs.close();
                    st.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}