/* Generated by nMigen Yosys 0.9+3746 (PyPI ver 0.9.post3746.dev31, git sha1 95c60866) */

(* \nmigen.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "nMigen" *)
module top(dat_r, dat_w, we, clk, rst, adr);
  (* src = "generate.py:12" *)
  input [3:0] adr;
  (* src = "/home/fede/nmigen/nmigen/hdl/ir.py:526" *)
  input clk;
  (* src = "generate.py:13" *)
  output [7:0] dat_r;
  (* src = "generate.py:14" *)
  input [7:0] dat_w;
  (* src = "generate.py:21" *)
  wire [3:0] mem_r_addr;
  (* src = "generate.py:21" *)
  wire [7:0] mem_r_data;
  (* src = "generate.py:22" *)
  wire [3:0] mem_w_addr;
  (* src = "generate.py:22" *)
  wire [7:0] mem_w_data;
  (* src = "generate.py:22" *)
  wire mem_w_en;
  (* src = "generate.py:24" *)
  wire [4:0] memo_r_addr;
  (* src = "generate.py:24" *)
  wire [23:0] memo_r_data;
  (* src = "generate.py:25" *)
  wire [4:0] memo_w_addr;
  (* src = "generate.py:25" *)
  wire [23:0] memo_w_data;
  (* src = "generate.py:25" *)
  wire memo_w_en;
  (* src = "/home/fede/nmigen/nmigen/hdl/ir.py:526" *)
  input rst;
  (* src = "generate.py:15" *)
  input we;
  reg [7:0] mem [15:0];
  $readmemh(mem8_h_dump.mem, mem);

  reg [3:0] _0_;
  always @(posedge clk) begin
    _0_ <= mem_r_addr;
    if (mem_w_en) mem[mem_w_addr] <= mem_w_data;
  end
  assign mem_r_data = mem[_0_];
  reg [23:0] memo [23:0];
  $readmemh(memo24_h_dump.mem, memo);

  reg [4:0] _1_;
  always @(posedge clk) begin
    _1_ <= memo_r_addr;
    if (memo_w_en) memo[memo_w_addr] <= memo_w_data;
  end
  assign memo_r_data = memo[_1_];
  assign memo_r_addr = 5'h00;
  assign memo_w_en = 1'h0;
  assign memo_w_addr = 5'h00;
  assign memo_w_data = 24'h000000;
  assign mem_w_en = we;
  assign mem_w_data = dat_w;
  assign mem_w_addr = adr;
  assign dat_r = mem_r_data;
  assign mem_r_addr = adr;
endmodule